#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <algorithm>
#include <numeric>
#include <array>
#include <vector>
#include <unordered_map>
#include <unordered_set>

struct Device
{
	using RegisterState = std::array<std::uintmax_t,6>;
	RegisterState Register;
	template< typename FunctorT , bool RegisterA = true, bool RegisterB = true>
	static void OpRegister( RegisterState& Registers, std::size_t A, std::size_t B, std::size_t C )
	{
		FunctorT Function;
		Registers[C] = Function(
			RegisterA ? Registers[A]:A,
			RegisterB ? Registers[B]:B
		);
	}
	const static std::unordered_map<std::uint32_t,std::size_t> MnemonicMap;

	typedef void(*Operation)( RegisterState&,std::size_t,std::size_t,std::size_t);
	constexpr static std::array<Operation,16> OpCodes = {{
		// addr
		OpRegister<std::plus<std::size_t>, true, true>,
		// addi
		OpRegister<std::plus<std::size_t>, true, false>,
		// mulr
		OpRegister<std::multiplies<std::size_t>,true,true>,
		// muli
		OpRegister<std::multiplies<std::size_t>,true,false>,
		// banr
		OpRegister<std::bit_and<std::size_t>,true,true>,
		// bani
		OpRegister<std::bit_and<std::size_t>,true,false>,
		// borr
		OpRegister<std::bit_or<std::size_t>,true,true>,
		// bori
		OpRegister<std::bit_or<std::size_t>,true,false>,
		// setr
		[]( RegisterState& Registers, std::size_t A, std::size_t, std::size_t C ) constexpr -> void
		{
			Registers[C] = Registers[A];
		},
		// seti
		[]( RegisterState& Registers, std::size_t A, std::size_t, std::size_t C ) constexpr -> void
		{
			Registers[C] = A;
		},
		// gtir
		OpRegister<std::greater<std::size_t>,false,true>,
		// gtri
		OpRegister<std::greater<std::size_t>,true,false>,
		// gtrr
		OpRegister<std::greater<std::size_t>,true,true>,
		// eqii
		OpRegister<std::equal_to<std::size_t>,false,true>,
		// eqri
		OpRegister<std::equal_to<std::size_t>,true,false>,
		// eqrr
		OpRegister<std::equal_to<std::size_t>,true,true>
	}};

	struct Instruction
	{
		std::size_t Opcode;
		std::array<std::size_t,3> Operands;
	};

	struct Program
	{
		std::size_t IPCRegister;
		std::vector<Instruction> Instructions;

		void Execute( RegisterState& CurRegisters ) const
		{
			std::unordered_set<std::uintmax_t> Seen;
			std::size_t Prev = 0;
			// while we have a valid instruction pointer
			while( CurRegisters[IPCRegister] < Instructions.size() )
			{
				std::size_t& ProgramCounter = CurRegisters[IPCRegister];
				Device::OpCodes[Instructions[ProgramCounter].Opcode](
					CurRegisters,
					Instructions[ProgramCounter].Operands[0],
					Instructions[ProgramCounter].Operands[1],
					Instructions[ProgramCounter].Operands[2]
				);
				++ProgramCounter;
				if( ProgramCounter == 28 )
				{
					// Part 1:
					// std::printf(
					// 	"%12zu\n",
					// 	CurRegisters[4]
					// );
					// break;

					// Part 2:
					if( Seen.find(CurRegisters[4]) == Seen.end())
					{
						Seen.insert(CurRegisters[4]);
					}
					else // Found a repeat
					{
						std::printf(
							"%12zu\n",
							Prev
						);
						break;
					}
					Prev = CurRegisters[4];
				}
				// Part 2
			}
		}
	};
};

const std::unordered_map<std::uint32_t,std::size_t> Device::MnemonicMap = {
	{'rdda',  0},
	{'idda',  1},
	{'rlum',  2},
	{'ilum',  3},
	{'rnab',  4},
	{'inab',  5},
	{'rrob',  6},
	{'irob',  7},
	{'rtes',  8},
	{'ites',  9},
	{'ritg', 10},
	{'irtg', 11},
	{'rrtg', 12},
	{'iiqe', 13},
	{'irqe', 14},
	{'rrqe', 15}
};

int main()
{ 
	Device::Program CurProgram;
	std::fscanf(
		stdin,
		"#ip %zu ",
		&CurProgram.IPCRegister
	);
	std::uint64_t CurMnemonic;
	Device::Instruction CurInstruction;
	while(
		std::fscanf(
			stdin,
			"%4s %zu %zu %zu ",
			reinterpret_cast<char*>(&CurMnemonic),
			&CurInstruction.Operands[0], &CurInstruction.Operands[1], &CurInstruction.Operands[2]
		) == 4
	)
	{
		CurInstruction.Opcode = Device::MnemonicMap.at(static_cast<std::uint32_t>(CurMnemonic));
		CurProgram.Instructions.push_back(CurInstruction);
	}

	Device::RegisterState Registers = {};
	CurProgram.Execute(Registers);
	return EXIT_SUCCESS;
}

